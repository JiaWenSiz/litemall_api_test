pipeline {
    // 1. 指定使用 Python 镜像作为运行环境
    agent {
        docker {
            image 'python:3.9-slim' 
            // 如果你需要 Docker in Docker，可以加 args，但这里只是跑测试，不需要
        }
    }

    stages {
        stage('API Test') {
            steps {
                sh '''
                    // 2. 在 Python 容器里，通常不需要 venv，直接 pip install 即可
                    // 但如果你想用也可以，这里直接简化流程
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

