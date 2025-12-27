from db_connection import get_connection

def start_quiz():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    score = 0
    print("\n===== ONLINE QUIZ =====\n")

    for q in questions:
        print(q[1])
        print("1.", q[2])
        print("2.", q[3])
        print("3.", q[4])
        print("4.", q[5])

        answer = int(input("Enter your answer (1-4): "))

        if answer == q[6]:
            score += 1
            print("Correct!\n")
        else:
            print("Wrong!\n")

    name = input("Enter your name: ")

    cursor.execute(
        "INSERT INTO results (username, score) VALUES (%s, %s)",
        (name, score)
    )
    conn.commit()

    print(f"\nQuiz Completed! {name}, Your Score: {score}/{len(questions)}")

    conn.close()

if __name__ == "__main__":
    start_quiz()
