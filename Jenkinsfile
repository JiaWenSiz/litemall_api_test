pipeline {
    // 1. 改回 agent any，利用 Jenkins 容器现有的环境
    agent any

    stages {
        stage('API Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    // 2. 关键修改：用点号 (.) 代替 source，因为 Jenkins 默认 shell 是 sh
                    . venv/bin/activate 
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            publishHTML(
                target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest API Test Report'
                ]
            )
        }
    }
}


