from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr, Global

# 这一行设置安装在本地的mathematica的核心地址，可设置为免费的wolfram云，即不需要本地安装mathematica。
wlpath = "D:\\Program_File\\Mathematica\\12.0\\MathKernel.exe"

sess = WolframLanguageSession(wlpath)  # mathmatica会话

# 以下代码块，按照mathematica语法输入待计算问题，此处为计算，10个都服从于N(1,3)的随机变量的和，所服从的分布及其期望方差。
exp = wlexpr('''
             Clear[MakeSeedSegment]
             MakeSeedSegment[radius_, angle_, n_Integer: 10, 
             connectingFunc_: Polygon, keepGridPoints_: False] := 
             Block[{t}, 
             t = Table[
             Line[{radius*r*{Cos[angle], Sin[angle]}, {radius*r, 0}}], {r, 0, 
             1, 1/n}];
             Join[If[TrueQ[keepGridPoints], t, {}], {GrayLevel[0.25], 
             connectingFunc@
             RandomSample[Flatten[t /. Line[{x_, y_}] :> {x, y}, 1]]}]];
             MakeMandala[opts : OptionsPattern[]] := 
             MakeMandala[
             MakeSymmetric[
             MakeSeedSegment[20, \[Pi]/12, 12, 
             RandomChoice[{Line, Polygon, BezierCurve, 
             FilledCurve[BezierCurve[#]] &}], False]], \[Pi]/6, opts];
             MakeMandala[seed_, angle_?NumericQ, opts : OptionsPattern[]] := 
             Graphics[GeometricTransformation[seed, 
             Table[RotationMatrix[a], {a, 0, 2 \[Pi] - angle, angle}]], opts];
             MakeSymmetric[seed_] := {seed, 
             GeometricTransformation[seed, ReflectionTransform[{0, 1}]]};
             n = 12;
             data = MapThread[
             If[#1, MakeMandala[MakeSeedSegment[10, #2, #3], #2], 
             MakeMandala[MakeSymmetric[MakeSeedSegment[10, #2, #3, #4, False]],
             2 #2]] &, {RandomChoice[{False, True}, n], 
             RandomChoice[{\[Pi]/7, \[Pi]/8, \[Pi]/6}, n], 
             RandomInteger[{8, 14}, n], 
             RandomChoice[{Line, Polygon, BezierCurve, 
             FilledCurve[BezierCurve[#]] &}, n]}]
             MapIndexed[
             Export["picture" <> Apply[IntegerString, #2] <> ".eps", #] &, data]
           ''')

sess.evaluate(exp)  # 会话启动，进行计算，类似tensorflow，计算后才有实际值
# 退出会话
sess.terminate()
# 退出程序后，输出epx格式文件
exit()
