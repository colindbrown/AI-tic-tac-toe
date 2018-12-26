# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 11:13:26 2015

@author: c_brown
"""
import time

def Board(list):
    print '   |   |   '
    print ' %s | %s | %s ' % (list['A1'],list['A2'],list['A3'])
    print '___|___|___'
    print '   |   |   '
    print ' %s | %s | %s ' % (list['B1'],list['B2'],list['B3'])
    print '___|___|___'
    print '   |   |   '
    print ' %s | %s | %s ' % (list['C1'],list['C2'],list['C3'])
    print '   |   |   '

def Intro():
    print 'Welcome to Tic Tac Toe!'
    time.sleep(1)
    print 'These are the positions. Remember them.'
    print ''
    time.sleep(1)
    print '    |    |    '
    print ' A1 | A2 | A3 ' 
    print '____|____|____'
    print '    |    |    '
    print ' B1 | B2 | B3 ' 
    print '____|____|____'
    print '    |    |    '
    print ' C1 | C2 | C3 '
    print '    |    |    '
    print ''
    time.sleep(1)
    print 'Are you ready? (Yes/No and then press Enter)'
    print''    
    if raw_input().lower() == 'yes':
        time.sleep(1)
        print''        
        return 'Yes'
    else:
        print ''         
        return 'No'
    
def CheckX(Positions):
    Vert = {'A':1, 'B':2, 'C':3, 1:'A', 2:'B', 3:'C'}    
    A = []
    B = []
    C = []  
    D = []
    E = []
    F = []
    G = ['A1','B2','C3']
    H = ['A3','B2','C1']
    for value in Positions:
        if Positions[value] == 'X':
            if value[0] == 'A':
                A.append(value[1])
            elif value[0] == 'B':
                B.append(value[1])
            elif value[0] == 'C':
                C.append(value[1])
    if len(A) == 2:
        if Positions['A%s' % (str(6-(int(A[0])+int(A[1]))))] == ' ':
            return 'A%s' % (str(6-(int(A[0])+int(A[1]))))
    if len(B) == 2:
        if Positions['B%s' % (str(6-(int(B[0])+int(B[1]))))] == ' ':
            return 'B%s' % (str(6-(int(B[0])+int(B[1]))))
    if len(C) == 2:
        if Positions['C%s' % (str(6-(int(C[0])+int(C[1]))))] == ' ':
            return 'C%s' % (str(6-(int(C[0])+int(C[1]))))
    if len(A) == 3:
        return 'X wins'
    if len(B) == 3:
        return 'X wins'
    if len(C) == 3:
        return 'X wins'
    for value in Positions:
        if Positions[value] == 'X':
            if value[1] == '1':
                D.append(value[0])
            elif value[1] == '2':
                E.append(value[0])
            elif value[1] == '3':
                F.append(value[0])
    if len(D) == 2:
        PosTot = 6        
        for item in D:
            PosTot -= Vert[item]
        if Positions['%s1' % (Vert[PosTot])] == ' ':
            return '%s1' % (Vert[PosTot])
    if len(E) == 2:
        PosTot = 6        
        for item in E:
            PosTot -= Vert[item]
        if Positions['%s2' % (Vert[PosTot])] == ' ':
            return '%s2' % (Vert[PosTot])
    if len(F) == 2:
        PosTot = 6        
        for item in F:
            PosTot -= Vert[item]
        if Positions['%s3' % (Vert[PosTot])] == ' ':
            return '%s3' % (Vert[PosTot])
    if len(D) == 3:
        return 'X wins'
    if len(E) == 3:
        return 'X wins'
    if len(F) == 3:
        return 'X wins'
    for value in Positions:
        if Positions[value] == 'X':
            if value in G:
                G.remove(value)
            if value in H:
                H.remove(value)
    if len(G) == 1 and len(H) != 0:
        if Positions[G[0]] == ' ':
            return G[0]
    if len(H) == 1 and len(G) != 0:
        if Positions[H[0]] == ' ':
            return H[0]
    if len(G) == 0:
        return 'X wins'
    if len(H) == 0:
        return 'X wins'

def CheckO(Positions):
    Vert = {'A':1, 'B':2, 'C':3, 1:'A', 2:'B', 3:'C'}    
    A = []
    B = []
    C = []  
    D = []
    E = []
    F = []
    G = ['A1','B2','C3']
    H = ['A3','B2','C1']
    for value in Positions:
        if Positions[value] == 'O':
            if value[0] == 'A':
                A.append(value[1])
            elif value[0] == 'B':
                B.append(value[1])
            elif value[0] == 'C':
                C.append(value[1])
    if len(A) == 2:
        if Positions['A%s' % (str(6-(int(A[0])+int(A[1]))))] == ' ':
            return 'A%s' % (str(6-(int(A[0])+int(A[1]))))
    if len(B) == 2:
        if Positions['B%s' % (str(6-(int(B[0])+int(B[1]))))] == ' ':
            return 'B%s' % (str(6-(int(B[0])+int(B[1]))))
    if len(C) == 2:
        if Positions['C%s' % (str(6-(int(C[0])+int(C[1]))))] == ' ':
            return 'C%s' % (str(6-(int(C[0])+int(C[1]))))
    for value in Positions:
        if Positions[value] == 'O':
            if value[1] == '1':
                D.append(value[0])
            elif value[1] == '2':
                E.append(value[0])
            elif value[1] == '3':
                F.append(value[0])
    if len(D) == 2:
        PosTot = 6        
        for item in D:
            PosTot -= Vert[item]
        if Positions['%s1' % (Vert[PosTot])] == ' ':
            return '%s1' % (Vert[PosTot])
    if len(E) == 2:
        PosTot = 6        
        for item in E:
            PosTot -= Vert[item]
        if Positions['%s2' % (Vert[PosTot])] == ' ':
            return '%s2' % (Vert[PosTot])
    if len(F) == 2:
        PosTot = 6        
        for item in F:
            PosTot -= Vert[item]
        if Positions['%s3' % (Vert[PosTot])] == ' ':
            return '%s3' % (Vert[PosTot])
    for value in Positions:
        if Positions[value] == 'O':
            if value in G:
                G.remove(value)
            if value in H:
                H.remove(value)
    if len(G) == 1:
        if Positions[G[0]] == ' ':
            return G[0]
    if len(H) == 1:
        if Positions[H[0]] == ' ':
            return H[0]

def Play():  
    turns = 0    
    Positions = {'A1':' ','A2':' ','A3':'X','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
    print 'I\'ll go first.'
    print ''    
    time.sleep(1)
    Board(Positions)
    time.sleep(1)
    print ''    
    while turns < 1:
        print 'Your turn'
        print 'Enter a position.'
        print ''
        time.sleep(1)
        check = 0
        while check == 0:
            move = str(raw_input().upper())
            print ''
            time.sleep(1)
            if move != 'A1' and move != 'A2' and move !='B1' and move !='B2' and move !='B3' and move !='C1' and move !='C2' and move !='C3':
                print '%s is not a sane input.'% (move)
                print ''
                time.sleep(1)
            if move == 'A1' or move == 'A2' or move =='B1' or move =='B2' or move =='B3' or move =='C1' or move =='C2' or move =='C3':
                if Positions[move] == ' ':
                    check += 1                    
                    turns += 1      
                    Positions[move] = 'O'
                    Board(Positions)
                    print ''
                    time.sleep(1)
                else:
                    print move + ' is not a valid input.'
                    print ''
                    time.sleep(1)
    while turns == 1:
        print 'My turn.'
        print ''
        time.sleep(1)
        if Positions['B2'] == 'O':
            Positions['C1'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
        if Positions['A1'] == 'O' or Positions['A2'] == 'O' or Positions['C1'] == 'O' or Positions['C2'] == 'O':
            Positions['C3'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
        if Positions['B1'] == 'O' or Positions['B3'] == 'O' or Positions['C3'] == 'O':
            Positions['A1'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
        print 'Your Turn'
        print ''
        time.sleep(1)
        check = 0
        while check == 0:
            move = str(raw_input().upper())
            print ''
            time.sleep(1)
            if move != 'A1' and move != 'A2' and move !='B1' and move !='B2' and move !='B3' and move !='C1' and move !='C2' and move !='C3':
                print '%s is not a valid input.'% (move)
                print ''
                time.sleep(1)
            if move == 'A1' or move == 'A2' or move =='B1' or move =='B2' or move =='B3' or move =='C1' or move =='C2' or move =='C3':
                if Positions[move] == ' ':
                    check += 1                    
                    turns += 1
                    Positions[move] = 'O'
                    Board(Positions)
                    print ''
                    time.sleep(1)
                else:
                    print move + ' is not a valid input.'
                    print ''
                    time.sleep(1)
    while turns >1 and turns < 8:        
        check = 0
        print'My turn.'
        print ''
        time.sleep(1)
        if CheckX(Positions) != None:
            Positions[CheckX(Positions)] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
            turns += 1
        elif CheckO(Positions) != None:
            Positions[CheckO(Positions)] = 'X'       
            Board(Positions)
            print ''
            time.sleep(1)
            turns += 1
        elif Positions['C1'] == 'O' or Positions['C2'] == 'O':
            Positions['A1'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
            turns += 1
        elif Positions['B1'] == 'O':
            Positions['C3'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
            turns += 1
        else:
            Positions['C1'] = 'X'
            Board(Positions)
            print ''
            time.sleep(1)
            turns += 1
        if CheckX(Positions) == 'X wins':
            check = 1
            turns = 12
            print 'X wins!'
            time.sleep(1)
        tienumb = 0
        for value in Positions:
            if Positions[value] != ' ':
                tienumb += 1
        if tienumb == 9:
            check = 1
            turns = 12
            print 'It\'s a tie!'
            time.sleep(1)
        if check == 0:
            print 'Your Turn'
            print ''
            time.sleep(1)
        while check == 0:
            move = str(raw_input().upper())
            print ''
            time.sleep(1)
            if move != 'A1' and move != 'A2' and move !='B1' and move !='B2' and move !='B3' and move !='C1' and move !='C2' and move !='C3':
                print '%s is not a valid input.'% (move)
                print ''
                time.sleep(1)
            if move == 'A1' or move == 'A2' or move =='B1' or move =='B2' or move =='B3' or move =='C1' or move =='C2' or move =='C3':
                if Positions[move] == ' ':
                    check += 1                    
                    turns += 1
                    time.sleep(1)        
                    Positions[move] = 'O'
                    Board(Positions)
                    print ''
                    time.sleep(1)
                else:
                    print move + ' is not a valid input.'
                    print ''
                    time.sleep(1)
        if turns == 12:
            print 'Do you want to play again?'
            print ''
            time.sleep(1)
            if raw_input().lower() == 'yes':
                print''
                time.sleep(1)
                Play()
             
if Intro() == 'Yes':
    Play()
