<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\Sync\StoreSyncBatchRequest;
use App\Services\SyncService;
use Illuminate\Http\JsonResponse;

class SyncController extends Controller
{
    public function __invoke(StoreSyncBatchRequest $request, SyncService $sync): JsonResponse
    {
        return response()->json(
            $sync->sync($request->user(), $request->validated('items')),
        );
    }
}
