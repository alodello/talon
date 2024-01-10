pipeline {
    agent any
    environment {
        // Укажите путь к вашему существующему виртуальному окружению
        PYTHON_ENV = 'C:\Users\alex2\AppData\Local\Programs\Python\Python310\Scripts\'
    }
    stages {
	stage('version'){
		steps{
			bat 'python --version'
		}
	}
        // stage('Run Tasks in Parallel') {
        //     parallel {
        //         stage('Task 1') {
        //             steps {
        //                 //echo "Executing Task 1"
        //                 // Add commands for Task 1
        //             }
        //         }
        //         stage('Task 2') {
        //             steps {
        //                 //echo "Executing Task 2"
        //                 // Add commands for Task 2
        //             }
        //         }
        //     }
        // }
    }
}
