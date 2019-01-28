pipeline {
  agent any
  stages {
    stage('Code Pull') {
      when {
        branch 'master'
      }
      steps {
        checkout scm
      }
    }
    stage('Tavern Tests') {
      steps {
        sh 'echo "Testing"'
      }
    }
  }
}