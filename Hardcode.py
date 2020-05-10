
#VARIABLES
names = [
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'ONETWO',
    'ONETHREE',
    'ONEFOUR',
    'TWOTHREE',
    'TWOFOUR',
    'THREEFOUR',
    'ONETWOTHREE',
    'ONETWOFOUR',
    'ONETHREEFOUR',
    'TWOTHREEFOUR',
    'ONETWOTHREEFOUR',

    'UP',
    'UPFORWARD',
    'FORWARD',
    'DOWNFORWARD',
    'DOWN',
    'DOWNBACK',
    'BACK',
    'UPBACK',

    'NEUTRAL',

    'UPHOLD',
    'UPFORWARDHOLD',
    'FORWARDHOLD',
    'DOWNFORWARDHOLD',
    'DOWNHOLD',
    'DOWNBACKHOLD',
    'BACKHOLD',
    'UPBACKHOLD',


    'SIDESTEPLEFT',
    'SIDESTEPRIGHT',
    'WHILESTANDING',

    'FOLLOW',
    'JUSTFRAME',
    'IN',
    'OUT',
    'TILDE',
]

filepath = {
    
    'ONE' :  r"\Images\Inputs\1.png",
    'TWO' : r"\Images\Inputs\2.png" ,
    'THREE' : r"\Images\Inputs\3.png",
    'FOUR' : r"\Images\Inputs\4.png",
    'ONETWO' : r"\Images\Inputs\12.png",
    'ONETHREE' : r"\Images\Inputs\13.png",
    'ONEFOUR' : r"\Images\Inputs\14.png",
    'TWOTHREE' : r"\Images\Inputs\23.png",
    'TWOFOUR' : r"\Images\Inputs\24.png",
    'THREEFOUR' : r"\Images\Inputs\34.png",
    'ONETWOTHREE' : r"\Images\Inputs\123.png",
    'ONETWOFOUR' : r"\Images\Inputs\124.png",
    'ONETHREEFOUR' : r"\Images\Inputs\134.png",
    'TWOTHREEFOUR': r"\Images\Inputs\234.png",
    'ONETWOTHREEFOUR': r"\Images\Inputs\1234.png",

    'UP' : r"\Images\Inputs\u.png",
    'UPFORWARD' : r"\Images\Inputs\uf.png",
    'FORWARD' : r"\Images\Inputs\f.png",
    'DOWNFORWARD' : r"\Images\Inputs\df.png",
    'DOWN' : r"\Images\Inputs\d.png",
    'DOWNBACK' : r"\Images\Inputs\db.png",
    'BACK' : r"\Images\Inputs\b.png",
    'UPBACK' : r"\Images\Inputs\ub.png",
    
    'NEUTRAL' : r"\Images\Inputs\n.png",
    
    'UPHOLD' : r"\Images\Inputs\uh.png",
    'UPFORWARDHOLD' : r"\Images\Inputs\ufh.png",
    'FORWARDHOLD' : r"\Images\Inputs\fh.png",
    'DOWNFORWARDHOLD' :  r"\Images\Inputs\dfh.png",
    'DOWNHOLD' :  r"\Images\Inputs\dh.png",
    'DOWNBACKHOLD' :  r"\Images\Inputs\dbh.png",
    'BACKHOLD' :  r"\Images\Inputs\bh.png",
    'UPBACKHOLD' :  r"\Images\Inputs\ubh.png",


    'SIDESTEPLEFT' : r"\Images\Inputs\ssl.png",
    'SIDESTEPRIGHT' : r"\Images\Inputs\ssr.png",
    'WHILESTANDING' : r"\Images\Inputs\ws.png",

    'FOLLOW' : r"\Images\Inputs\follow.png",
    'JUSTFRAME' : r"\Images\Inputs\jf.png",
    'IN' : r"\Images\Inputs\in.png",
    'OUT' : r"\Images\Inputs\out.png",
    'TILDE' : r"\Images\Inputs\tilde.png",
}

display = {

    'ONE' : '1',
    'TWO' : '2',
    'THREE' : '3',
    'FOUR' : '4',
    'ONETWO' : '1+2',
    'ONETHREE' :'1+3',
    'ONEFOUR' : '1+4',
    'TWOTHREE' : '2+3',
    'TWOFOUR' : '2+4',
    'THREEFOUR' : '3+4',
    'ONETWOTHREE' : '1+2+3',
    'ONETWOFOUR' : '1+2+4',
    'ONETHREEFOUR' : '1+3+4',
    'TWOTHREEFOUR': '2+3+4',
    'ONETWOTHREEFOUR': '1+2+3+4',

    'UP' : 'u',
    'UPFORWARD' : 'u/f',
    'FORWARD' : 'f',
    'DOWNFORWARD' : 'd/f',
    'DOWN' : 'd',
    'DOWNBACK' : 'd/b',
    'BACK' : 'b',
    'UPBACK' : 'u/b',

    'NEUTRAL' : 'N',

    'UPHOLD' : 'U',
    'UPFORWARDHOLD' : 'U/F',
    'FORWARDHOLD' : 'F',
    'DOWNFORWARDHOLD' :  'D/F',
    'DOWNHOLD' :  'D',
    'DOWNBACKHOLD' :  'D/B',
    'BACKHOLD' :  'B',
    'UPBACKHOLD' :  'U/B',


    'SIDESTEPLEFT' : 'SSL',
    'SIDESTEPRIGHT' : 'SSR',
    'WHILESTANDING' : 'WS',

    'FOLLOW' : ' > ',
    'JUSTFRAME' : ":",
    'IN' : "(",
    'OUT' : ")",
    'TILDE' : "~",
}

fileDisplay = {

    'ONE' : '1',
    'TWO' : '2',
    'THREE' : '3',
    'FOUR' : '4',
    'ONETWO' : '1+2',
    'ONETHREE' :'1+3',
    'ONEFOUR' : '1+4',
    'TWOTHREE' : '2+3',
    'TWOFOUR' : '2+4',
    'THREEFOUR' : '3+4',
    'ONETWOTHREE' : '1+2+3',
    'ONETWOFOUR' : '1+2+4',
    'ONETHREEFOUR' : '1+3+4',
    'TWOTHREEFOUR': '2+3+4',
    'ONETWOTHREEFOUR': '1+2+3+4',

    'UP' : 'u',
    'UPFORWARD' : 'uf',
    'FORWARD' : 'f',
    'DOWNFORWARD' : 'df',
    'DOWN' : 'd',
    'DOWNBACK' : 'db',
    'BACK' : 'b',
    'UPBACK' : 'ub',
    
    'NEUTRAL' : 'N',
    
    'UPHOLD' : 'U',
    'UPFORWARDHOLD' : 'UF',
    'FORWARDHOLD' : 'F',
    'DOWNFORWARDHOLD' :  'DF',
    'DOWNHOLD' :  'D',
    'DOWNBACKHOLD' :  'DB',
    'BACKHOLD' :  'B',
    'UPBACKHOLD' :  'UB',

    'SIDESTEPLEFT' : 'SSL',
    'SIDESTEPRIGHT' : 'SSR',
    'WHILESTANDING' : 'WS',

    'FOLLOW' : '_',
    'JUSTFRAME' : "-",
    'IN' : "(",
    'OUT' : ")",
    'TILDE' : "~",
}

buttonLayout = {

    'ONE' : (3,0),
    'TWO' : (3,1),
    'THREE' : (3,2),
    'FOUR' : (3,3),
    'ONETWO' : (3,4),
    'ONETHREE' : (3,5),
    'ONEFOUR' : (3,6),
    'TWOTHREE' : (3,7),
    'TWOFOUR' : (3,8),
    'THREEFOUR' : (3,9),
    'ONETWOTHREE' :(3,10),
    'ONETWOFOUR' : (3,11),
    'ONETHREEFOUR' : (3,12),
    'TWOTHREEFOUR': (3,13),
    'ONETWOTHREEFOUR': (3,14),

    'UP' : (4,0),
    'UPFORWARD' : (4,1),
    'FORWARD' : (4,2),
    'DOWNFORWARD' : (4,3),
    'DOWN' : (4,4),
    'DOWNBACK' : (4,5),
    'BACK' : (4,6),
    'UPBACK' : (4,7),
    
    'NEUTRAL' : (4,8),
    
    'UPHOLD' : (4,9),
    'UPFORWARDHOLD' : (4,10),
    'FORWARDHOLD' : (4,11),
    'DOWNFORWARDHOLD' :  (4,12),
    'DOWNHOLD' :  (4,13),
    'DOWNBACKHOLD' :  (4,14),
    'BACKHOLD' :  (4,15),
    'UPBACKHOLD' :  (4,16),

    'SIDESTEPLEFT' : (6,0),
    'SIDESTEPRIGHT' : (6,1),
    'WHILESTANDING' : (6,2),

    'FOLLOW' : (5,0),
    'JUSTFRAME' : (5,1),
    'IN' : (5,2),
    'OUT' : (5,3),
    'TILDE' : (5,4)
}