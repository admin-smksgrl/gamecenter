/**
 * Renderer diagram alur sederhana untuk blok `diagram` (plan §4.1).
 *
 * Kenapa tidak memakai pustaka Mermaid langsung: pada lingkungan aplikasi ini
 * Mermaid 11/12 mengukur lebar label sekitar 10× terlalu besar, sehingga
 * diagram tersebar dengan kotak kecil dan ruang kosong raksasa (bug yang juga
 * terlihat pada diagram di halaman Panduan). Supaya materi tetap terbaca dan
 * ringan (tanpa 660 kB chunk), blok `diagram` memakai parser + tata letak SVG
 * milik sendiri untuk subset sintaks Mermaid yang dipakai materi:
 *
 *     graph TD            // atau LR
 *       A[Kotak] --> B(Kotak bulat)
 *       B -->|label| C{Keputusan}
 *       C --> D
 *
 * Fitur lain (subgraph, classDef, style, klik) diabaikan. Bila kode tidak bisa
 * diurai, renderer mengembalikan `null` dan pemanggil menampilkan kode aslinya.
 */

export type DiagramDirection = 'TD' | 'LR';

export interface DiagramNode {
    id: string;
    label: string;
    shape: 'rect' | 'round' | 'diamond';
}

export interface DiagramEdge {
    from: string;
    to: string;
    label?: string;
}

export interface ParsedDiagram {
    direction: DiagramDirection;
    nodes: DiagramNode[];
    edges: DiagramEdge[];
}

const NODE_TOKEN = /^([A-Za-z0-9_.-]+)(?:\[([^\]]*)\]|\(([^)]*)\)|\{([^}]*)\})?$/;
const EDGE_SPLIT = /\s*-{2,3}>\s*|\s*-{3}\s*/;

function nodeShape(token: string): { id: string; label?: string; shape: DiagramNode['shape'] } | null {
    const match = NODE_TOKEN.exec(token.trim());

    if (!match) {
        return null;
    }

    const [, id, square, round, diamond] = match;

    if (square !== undefined) {
        return { id, label: square, shape: 'rect' };
    }

    if (round !== undefined) {
        return { id, label: round, shape: 'round' };
    }

    if (diamond !== undefined) {
        return { id, label: diamond, shape: 'diamond' };
    }

    return { id, shape: 'rect' };
}

/**
 * Mengurai subset sintaks `graph`/`flowchart` Mermaid. Mengembalikan `null`
 * bila tidak ada node sama sekali (kode dianggap bukan diagram alur).
 */
export function parseFlowchart(code: string): ParsedDiagram | null {
    const lines = code
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter((line) => line !== '' && !line.startsWith('%%'));

    let direction: DiagramDirection = 'TD';
    const nodes = new Map<string, DiagramNode>();
    const edges: DiagramEdge[] = [];

    function touch(parsed: { id: string; label?: string; shape: DiagramNode['shape'] }) {
        const existing = nodes.get(parsed.id);

        if (existing) {
            if (parsed.label !== undefined && parsed.label !== '') {
                existing.label = parsed.label;
                existing.shape = parsed.shape;
            }

            return;
        }

        nodes.set(parsed.id, {
            id: parsed.id,
            label: parsed.label ?? parsed.id,
            shape: parsed.shape,
        });
    }

    for (const line of lines) {
        const header = /^(?:graph|flowchart)\s+(TD|TB|LR)$/i.exec(line);

        if (header) {
            direction = header[1].toUpperCase() === 'LR' ? 'LR' : 'TD';
            continue;
        }

        if (/^(?:subgraph|end|classDef|class|style|linkStyle|click)\b/i.test(line)) {
            continue;
        }

        const segments = line.split(EDGE_SPLIT);

        if (segments.length === 1) {
            const parsed = nodeShape(segments[0]);

            if (parsed) {
                touch(parsed);
            }

            continue;
        }

        for (let i = 0; i < segments.length - 1; i += 1) {
            let rawFrom = segments[i].trim();
            let rawTo = segments[i + 1].trim();
            let label: string | undefined;

            // `A -->|teks| B`: label menempel di ujung kanan segmen kiri.
            const labelInFrom = /\|([^|]*)\|\s*$/.exec(rawFrom);

            if (labelInFrom) {
                label = labelInFrom[1].trim();
                rawFrom = rawFrom.slice(0, labelInFrom.index).trim();
            }

            const labelInTo = /^\|([^|]*)\|\s*/.exec(rawTo);

            if (labelInTo) {
                label = labelInTo[1].trim();
                rawTo = rawTo.slice(labelInTo[0].length).trim();
            }

            const from = nodeShape(rawFrom);
            const to = nodeShape(rawTo);

            if (!from || !to) {
                continue;
            }

            touch(from);
            touch(to);
            edges.push({ from: from.id, to: to.id, label });
        }
    }

    if (nodes.size === 0) {
        return null;
    }

    return { direction, nodes: [...nodes.values()], edges };
}

export interface DiagramLayout {
    width: number;
    height: number;
    nodes: Array<{
        node: DiagramNode;
        x: number;
        y: number;
        width: number;
        height: number;
    }>;
    edges: Array<{
        edge: DiagramEdge;
        points: Array<[number, number]>;
        labelPosition: [number, number] | undefined;
    }>;
}

const CHAR_WIDTH = 7.1;
const NODE_HEIGHT = 34;
const DIAMOND_HEIGHT = 46;
const GAP_SIBLING = 26;
const GAP_RANK = 46;
const PADDING = 12;
const MAX_NODE_WIDTH = 240;
const NODE_PADDING = 26;
const LINE_HEIGHT = 15;

function wrapLabel(label: string): string[] {
    const maxChars = Math.max(
        Math.floor((MAX_NODE_WIDTH - NODE_PADDING) / CHAR_WIDTH),
        8,
    );
    const words = label.split(/\s+/).filter(Boolean);
    const lines: string[] = [];
    let current = '';

    for (const word of words) {
        const candidate = current ? `${current} ${word}` : word;

        if (candidate.length > maxChars && current) {
            lines.push(current);
            current = word;
        } else {
            current = candidate;
        }
    }

    if (current) {
        lines.push(current);
    }

    // Kata tunggal yang lebih panjang dari kotak dipotong agar tidak meluber.
    return lines.map((line) =>
        line.length > maxChars ? line.slice(0, maxChars) : line,
    );
}

function nodeSize(node: DiagramNode): { width: number; height: number } {
    const lines = wrapLabel(node.label);
    const longest = Math.max(...lines.map((line) => line.length), 1);
    const width = Math.min(
        Math.max(longest * CHAR_WIDTH + NODE_PADDING, 84),
        MAX_NODE_WIDTH,
    );
    const height = Math.max(NODE_HEIGHT, lines.length * LINE_HEIGHT + 16);

    return {
        width: node.shape === 'diamond' ? width + 26 : width,
        height:
            node.shape === 'diamond'
                ? Math.max(DIAMOND_HEIGHT, height + 12)
                : height,
    };
}

/**
 * Penataan sederhana: node dikelompokkan per "rank" (jarak terpanjang dari
 * akar), lalu dipusatkan. Cukup untuk diagram alur materi, dan hasilnya stabil
 * tanpa algoritma dagre.
 */
export function layoutDiagram(diagram: ParsedDiagram): DiagramLayout {
    const ranks = new Map<string, number>();
    const incoming = new Map<string, number>();

    diagram.nodes.forEach((node) => {
        ranks.set(node.id, 0);
        incoming.set(node.id, 0);
    });

    diagram.edges.forEach((edge) => {
        incoming.set(edge.to, (incoming.get(edge.to) ?? 0) + 1);
    });

    // Relaksasi berulang; bila ada siklus, batasi jumlah putaran.
    for (let round = 0; round < diagram.nodes.length; round += 1) {
        let changed = false;

        for (const edge of diagram.edges) {
            const next = (ranks.get(edge.from) ?? 0) + 1;

            if (next > (ranks.get(edge.to) ?? 0) && next < diagram.nodes.length) {
                ranks.set(edge.to, next);
                changed = true;
            }
        }

        if (!changed) {
            break;
        }
    }

    const rows = new Map<number, DiagramNode[]>();

    diagram.nodes.forEach((node) => {
        const rank = ranks.get(node.id) ?? 0;

        if (!rows.has(rank)) {
            rows.set(rank, []);
        }

        rows.get(rank)!.push(node);
    });

    const orderedRanks = [...rows.keys()].sort((a, b) => a - b);
    const placed = new Map<string, DiagramLayout['nodes'][number]>();

    // Lebar/tinggi baris dihitung dulu supaya tiap rank bisa dipusatkan.
    const rowInfo = orderedRanks.map((rank) => {
        const row = rows.get(rank)!;
        const sizes = row.map(nodeSize);
        const length = sizes.reduce(
            (sum, size, index) =>
                sum +
                (diagram.direction === 'TD' ? size.width : size.height) +
                (index === 0 ? 0 : GAP_SIBLING),
            0,
        );
        const thickness = Math.max(
            ...sizes.map((size) =>
                diagram.direction === 'TD' ? size.height : size.width,
            ),
        );

        return { rank, row, sizes, length, thickness };
    });

    const maxLength = Math.max(...rowInfo.map((info) => info.length));
    let cursor = PADDING;

    for (const info of rowInfo) {
        let along = (maxLength - info.length) / 2;

        info.row.forEach((node, index) => {
            const size = info.sizes[index];
            const cross = cursor + (info.thickness - (diagram.direction === 'TD' ? size.height : size.width)) / 2;

            placed.set(
                node.id,
                diagram.direction === 'TD'
                    ? {
                          node,
                          x: PADDING + along,
                          y: PADDING + cross,
                          width: size.width,
                          height: size.height,
                      }
                    : {
                          node,
                          x: PADDING + cross,
                          y: PADDING + along,
                          width: size.width,
                          height: size.height,
                      },
            );

            along +=
                (diagram.direction === 'TD' ? size.width : size.height) +
                GAP_SIBLING;
        });

        cursor += info.thickness + GAP_RANK;
    }

    const layoutNodes = [...placed.values()];
    const width = Math.max(
        ...layoutNodes.map((item) => item.x + item.width),
        PADDING * 2,
    );
    const height = Math.max(
        ...layoutNodes.map((item) => item.y + item.height),
        PADDING * 2,
    );

    const edges: DiagramLayout['edges'] = diagram.edges
        .map((edge) => {
            const from = placed.get(edge.from);
            const to = placed.get(edge.to);

            if (!from || !to) {
                return null;
            }

            const points: Array<[number, number]> =
                diagram.direction === 'TD'
                    ? [
                          [from.x + from.width / 2, from.y + from.height],
                          [to.x + to.width / 2, to.y],
                      ]
                    : [
                          [from.x + from.width, from.y + from.height / 2],
                          [to.x, to.y + to.height / 2],
                      ];

            const labelPosition: [number, number] | undefined = edge.label
                ? [
                      (points[0][0] + points[1][0]) / 2,
                      (points[0][1] + points[1][1]) / 2,
                  ]
                : undefined;

            return { edge, points, labelPosition };
        })
        .filter((item): item is DiagramLayout['edges'][number] => item !== null);

    // `filter` di atas sudah membuang `null`; tipe eksplisit menjaga TS tetap
    // tahu bahwa setiap butir punya `labelPosition` (mungkin undefined).

    return { width, height, nodes: layoutNodes, edges };
}

function escapeXml(value: string): string {
    return value
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
}

/**
 * Menghasilkan string SVG siap sisip. Semua teks di-escape supaya kode diagram
 * tidak bisa menyelundupkan markup (plan §7 keamanan konten).
 */
export function renderDiagramSvg(code: string): string | null {
    const parsed = parseFlowchart(code);

    if (!parsed) {
        return null;
    }

    const layout = layoutDiagram(parsed);
    const markerId = 'diagram-arrow';

    const edgeMarkup = layout.edges
        .map(({ points }) => {
            const [start, end] = points;
            const midY = (start[1] + end[1]) / 2;
            const midX = (start[0] + end[0]) / 2;

            const path =
                parsed.direction === 'TD'
                    ? `M ${start[0]} ${start[1]} C ${start[0]} ${midY}, ${end[0]} ${midY}, ${end[0]} ${end[1]}`
                    : `M ${start[0]} ${start[1]} C ${midX} ${start[1]}, ${midX} ${end[1]}, ${end[0]} ${end[1]}`;

            return `<path d="${path}" class="diagram-edge" marker-end="url(#${markerId})" />`;
        })
        .join('');

    const labelMarkup = layout.edges
        .filter(({ edge }) => edge.label)
        .map(({ edge, labelPosition }) => {
            if (!labelPosition) {
                return '';
            }

            return `<text x="${labelPosition[0]}" y="${labelPosition[1] - 4}" text-anchor="middle" class="diagram-edge-label">${escapeXml(
                edge.label!,
            )}</text>`;
        })
        .join('');

    const nodeMarkup = layout.nodes
        .map(({ node, x, y, width, height }) => {
            const lines = wrapLabel(node.label);
            const centerX = x + width / 2;
            const startY =
                y + height / 2 - ((lines.length - 1) * LINE_HEIGHT) / 2 + 4;
            const text = `<text x="${centerX}" text-anchor="middle" class="diagram-node-label">${lines
                .map(
                    (line, index) =>
                        `<tspan x="${centerX}" y="${startY + index * LINE_HEIGHT}">${escapeXml(
                            line,
                        )}</tspan>`,
                )
                .join('')}</text>`;

            if (node.shape === 'diamond') {
                const cx = x + width / 2;
                const cy = y + height / 2;

                return `<g><path d="M ${cx} ${cy - height / 2} L ${cx + width / 2} ${cy} L ${cx} ${cy + height / 2} L ${cx - width / 2} ${cy} Z" class="diagram-node" />${text}</g>`;
            }

            const radius = node.shape === 'round' ? height / 2 : 8;

            return `<g><rect x="${x}" y="${y}" width="${width}" height="${height}" rx="${radius}" class="diagram-node" />${text}</g>`;
        })
        .join('');

    return [
        `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${Math.round(layout.width)} ${Math.round(
            layout.height,
        )}" width="${Math.round(layout.width)}" height="${Math.round(
            layout.height,
        )}" role="img">`,
        `<defs><marker id="${markerId}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" class="diagram-arrow" /></marker></defs>`,
        edgeMarkup,
        labelMarkup,
        nodeMarkup,
        '</svg>',
    ].join('');
}
