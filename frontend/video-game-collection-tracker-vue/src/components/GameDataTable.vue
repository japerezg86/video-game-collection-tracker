<template>
    <DataTable :value="games" v-model:selection="selections" sortMode="multiple" dataKey="uuid">
        <Column selectionMode="multiple" headerStyle="width: 3em"></Column>
        <Column field="title" header="Title" :sortable="true"></Column>
        <Column field="summary" header="Summary" :sortable="true"></Column>
        <Column field="platform" header="Platform" :sortable="true"></Column>
        <Column field="developer" header="Developer" :sortable="true"></Column>
        <Column field="publisher" header="Publisher" :sortable="true"></Column>
        <Column field="owned" header="Owned" :sortable="true"></Column>
        <Column field="rating" header="Rating" :sortable="true"></Column>
        <Column field="progress" header="Status" :sortable="true"></Column>
    </DataTable>
</template>
<style></style>

<script lang="ts">
import { defineComponent, onMounted, ref, watchEffect } from "vue";
import videoGameService from "../service/VideoGameService";
import { selectedGameIds, useGetGames } from "../state/gamesState";

export default defineComponent({
    name: "GameDataTable",
    setup() {
        const { games } = useGetGames();
        const selections = ref<any[]>([]);
        watchEffect(() => {
            selectedGameIds.value = selections.value.map(e => e.uuid);
        });
        return {
            games,
            selections
        };
    },
});
</script>