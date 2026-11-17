import type { MaterialBlock } from '@/lib/material/blocks';
import { materialBlockKey } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import ChallengeBlockView from '@/Components/Material/Blocks/ChallengeBlock';
import CheckpointBlockView from '@/Components/Material/Blocks/CheckpointBlock';
import LabelBlockView from '@/Components/Material/Blocks/LabelBlock';
import ScenarioBlockView from '@/Components/Material/Blocks/ScenarioBlock';
import {
    ChartBlockView,
    DiagramBlockView,
    HotspotsBlockView,
    TimelineBlockView,
} from '@/Components/Material/Blocks/VisualBlocks';
import {
    CategorizeBlockView,
    SortBlockView,
} from '@/Components/Material/Blocks/DragSortBlock';
import {
    FlashcardsBlockView,
    GlossaryBlockView,
} from '@/Components/Material/Blocks/RecallBlocks';
import {
    CalloutBlockView,
    CodeBlockView,
    HeadingBlockView,
    ListBlockView,
    ParagraphBlockView,
    TableBlockView,
} from '@/Components/Material/Blocks/TextBlocks';

/**
 * Merangkai `blocks` materi menjadi elemen React (plan §3.3).
 *
 * Fase 1 mengenali blok teks; Fase 2 menambah glosarium, kartu hafalan, dan
 * tiga blok aktivitas yang dinilai (`checkpoint`, `sort`, `categorize`).
 * Fase 3 menambah visual (`diagram`, `chart`, `hotspots`, `timeline`) dan
 * aktivitas `label`; Fase 4 menutup `scenario` dan `challenge` sehingga semua
 * tipe blok pada skema sudah punya renderer.
 */
function PendingBlockView({ type }: { type: string }) {
    return (
        <p className="rounded-lg border border-dashed border-rule bg-canvas/60 px-2.5 py-1.5 text-[10px] font-semibold text-ink/40">
            {type} — belum tersedia di versi ini.
        </p>
    );
}

function renderBlock(
    block: MaterialBlock,
    materialId: number,
    onRecord?: (payload: MaterialBlockPayload) => void,
) {
    switch (block.type) {
        case 'heading':
            return <HeadingBlockView block={block} />;
        case 'paragraph':
            return <ParagraphBlockView block={block} />;
        case 'list':
            return <ListBlockView block={block} />;
        case 'table':
            return <TableBlockView block={block} />;
        case 'callout':
            return <CalloutBlockView block={block} />;
        case 'code':
            return <CodeBlockView block={block} />;
        case 'glossary':
            return <GlossaryBlockView block={block} />;
        case 'flashcards':
            return <FlashcardsBlockView block={block} />;
        case 'checkpoint':
            return (
                <CheckpointBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        case 'sort':
            return (
                <SortBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        case 'categorize':
            return (
                <CategorizeBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        case 'diagram':
            return <DiagramBlockView block={block} />;
        case 'chart':
            return <ChartBlockView block={block} />;
        case 'hotspots':
            return <HotspotsBlockView block={block} />;
        case 'timeline':
            return <TimelineBlockView block={block} />;
        case 'label':
            return (
                <LabelBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        case 'scenario':
            return (
                <ScenarioBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        case 'challenge':
            return (
                <ChallengeBlockView
                    block={block}
                    materialId={materialId}
                    onRecord={onRecord}
                />
            );
        default:
            // Semua tipe pada skema sudah punya renderer; cabang ini hanya
            // jaring pengaman bila data lama memuat tipe di luar skema.
            return (
                <PendingBlockView
                    type={(block as { type?: string }).type ?? 'blok'}
                />
            );
    }
}

export default function BlockRenderer({
    blocks,
    materialId,
    onRecord,
}: {
    blocks: MaterialBlock[];
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}) {
    if (blocks.length === 0) {
        return null;
    }

    return (
        <div className="material-prose">
            {blocks.map((block, index) => (
                <div key={materialBlockKey(block, index)}>
                    {renderBlock(block, materialId, onRecord)}
                </div>
            ))}
        </div>
    );
}
