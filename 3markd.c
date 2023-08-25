#include <stdio.h>
#define NUMBER_STUDENTS 3
#define NUMBER_SEMESTERS 6
#define NUMBER_SUBJECTS 5

typedef struct {
    int rollNo;
    char name[50];
    int marks[NUMBER_SEMESTERS][NUMBER_SUBJECTS];
    float percentage[NUMBER_SEMESTERS];
} Student;

void calculatePercentage(Student *student) {
    for (int i = 0; i < NUMBER_SEMESTERS; i++) {
        int totalMarks = 0;
        for (int j = 0; j < NUMBER_SUBJECTS; j++) {
            totalMarks += student->marks[i][j];
        }
        student->percentage[i] = (float)totalMarks / NUMBER_SUBJECTS;
    }
}

void printResult(float percentage) {
    if (percentage <= 40) {
        printf("Result: Fail\n");
    } else if (percentage >= 60 && percentage < 80) {
        printf("Result: First Class\n");
    } else if (percentage >= 80 && percentage <= 90) {
        printf("Result: First Class with Distinction\n");
    } else if (percentage > 90 && percentage <= 100) {
        printf("Result: Outstanding\n");
    }
}

int main() {
    Student students[NUMBER_STUDENTS];
    for (int i = 0; i < NUMBER_STUDENTS; i++) {
        printf("Enter details for student %d:\n", i + 1);
        printf("Roll No: ");
        scanf("%d", &students[i].rollNo);
        printf("Name: ");
        scanf("%s", students[i].name);

        for (int j = 0; j < NUMBER_SEMESTERS; j++) {
            printf("\nEnter marks for Semester %d in terms of 100:\n", j + 1);
            for (int k = 0; k < NUMBER_SUBJECTS; k++) {
                printf("Subject %d: ", k + 1);
                scanf("%d", &students[i].marks[j][k]);
            }
        }
    }
    for (int i = 0; i < NUMBER_STUDENTS; i++) {
        calculatePercentage(&students[i]);
        printf("\nDetails for student %d (Roll No: %d):\n", i + 1, students[i].rollNo);
        printf("Name: %s\n", students[i].name);
        for (int j = 0; j < NUMBER_SEMESTERS; j++) {
                printf("Semester %d:\n", j + 1);
                printf("Percentage: %.2f\n", students[i].percentage[j]);
                printResult(students[i].percentage[j]);
        }
    }
int eligibleCount = 0;
for (int i = 0; i < NUMBER_STUDENTS; i++) {
        if (students[i].percentage[NUMBER_SEMESTERS - 1] >= 40) {
            eligibleCount++;
        }
    }
    printf("\nNumber of students eligible for the degree: %d\n", eligibleCount);
    return 0;
}

