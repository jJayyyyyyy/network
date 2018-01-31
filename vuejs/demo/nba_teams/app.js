var apiURL = 'http://matchweb.sports.qq.com/rank/team?competitionId=100000&from=NBA_PC'

var nbateam

var demo = new Vue({
  el: '#demo',
  data: {
    branches: ['atlantic', 'central', 'east', 'eastsouth', 'pacific', 'west', 'westnorth', 'westsouth'],
    currentBranch: 'atlantic',
    commits: [0]
  },

  created: function () {
      var js = document.createElement('script')
      var head = document.getElementsByTagName('head')[0]
      js.src = apiURL+'&callback=refreshTeam'
      head.appendChild(js)
  },

  watch: {
    currentBranch: 'getBranch'
  },

  methods: {
    getBranch: function(){
      this.commits = teams[this.currentBranch]
      console.log(this.currentBranch)
    }
  }
})

function refreshTeam(data){
  teams = data[1]
  demo.commits = teams['atlantic']
  console.log(data)
}
