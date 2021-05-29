import { createStore } from 'vuex'

export default createStore({
  state: {
    content: "",
    Output: "",
    indexArr: [],
    coloumArr: [],
    tableData: []
  },
  mutations: {
    contentChange(state,newContent){
      state.content = newContent;
    },
    OutputChange(state,newOutput){
      state.Output = newOutput
    },
    indexArrChange(state,newIndexArr){
      state.indexArr = newIndexArr
    },
    coloumArrChange(state,newColoumArr){
      state.coloumArr = newColoumArr
    },
    tableDataChange(state,newTableData){
      state.tableData = newTableData
    },
  },
  actions: {
  },
  modules: {
  }
})
