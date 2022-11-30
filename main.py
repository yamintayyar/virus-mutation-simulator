import random

class virus:

    def __init__(self, len, myDNA=""):
        self.DNA = myDNA
        self.length = len

        if myDNA == "":
            for i in range(len):
                self.DNA += {0: 'A', 1: 'G', 2: 'T', 3: 'C'}[random.randint(0, 3)]  # adds either A,G,T, or C randomly

    def getDNA(self):
        return self.DNA

    def getLength(self):
        return self.length

    def replicate(self):
        p = random.randint(1, 100)

        if p > 94:

            i = random.randint(0, self.length - 1)
            mutatedDNA = self.DNA[:i] + {0: 'A', 1: 'G', 2: 'T', 3: 'C'}[random.randint(0, 3)] + self.DNA[i + 1:]

            return virus(self.length, mutatedDNA)

        return virus(self.length, self.DNA)


def find_mutation(virus1, virus2):
    dna1 = virus1.getDNA()
    dna2 = virus2.getDNA()

    s = ""

    for i in range(virus1.getLength()):
        if dna1[i] == dna2[i]:
            s += " "
        else:
            s += "^"

    return s


def virus_mutation():
    r = True

    while r:
        name = input("Name of virus: ")
        l = int(input("Length of virus DNA: "))

        my_virus = virus(l)

        original_virus = my_virus

        print(f"Original DNA sequence: {my_virus.getDNA()}")

        n = int(input('How many times to replicate?'))

        for i in range(n):
            my_virus = my_virus.replicate()

            print(f"Replica [{i + 1:3}] DNA Sequence: {my_virus.getDNA()}")

        m = find_mutation(original_virus, my_virus)

        print(f"""Comparing latest {name} to the original {name}.
{original_virus.getDNA()}
{my_virus.getDNA()}
{m}""")

        m_count = m.count('^')

        if m_count == 0:
            print('No mutations detected.')
        elif m_count <= 5:
            print(f"{m_count} mutations -- virus is the same.")
        else:
            print(f"{m_count} mutations -- a *new* virus has been created.")

        r = input("Try again? ").lower() == "y"


virus_mutation()
