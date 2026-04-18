pipeline {
    agent any

    stages {
        stage('API Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
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
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest 接口自动化测试报告'
            ])
        }
    }
}
