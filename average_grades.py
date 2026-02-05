"""Υπολογισμός μέσου όρου βαθμών για 10 μαθητές."""


def main() -> None:
    grades: list[float] = []

    for i in range(1, 11):
        while True:
            try:
                grade = float(input(f"Δώσε τον βαθμό του μαθητή {i}: "))
                if 0 <= grade <= 20:
                    grades.append(grade)
                    break
                print("Ο βαθμός πρέπει να είναι από 0 έως 20.")
            except ValueError:
                print("Μη έγκυρη τιμή. Προσπάθησε ξανά.")

    average = sum(grades) / len(grades)
    print(f"Ο μέσος όρος των 10 μαθητών είναι: {average:.2f}")


if __name__ == "__main__":
    main()
