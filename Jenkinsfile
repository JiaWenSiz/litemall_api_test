pipeline {
    agent any

    stages {
        // 1. 显式拉取代码（使用 SSH）
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // 2. 运行测试
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
            
            // 3. 发布报告（修正语法）
            publishHTML(
                target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest API Test Report'  // 改为英文
                ]
            )
        }
    }
}
