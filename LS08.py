def get_class(subject: str, num: int) -> None:
    print(
        f"I'm currently in {subject}{num}, but next semester I'm taking {subject}{num+100}!"
    )


get_class(subject="COMP", num=110)
