''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT


def main():
    print(sorted(list(map(int, list(input()))))[-1], end='')


 # Write code here

main()

