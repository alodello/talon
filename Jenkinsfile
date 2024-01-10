pipeline {
    agent any    
    stages {
	stage('version'){
		steps{
			bat 'pytest test_mails_existence.py'
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
