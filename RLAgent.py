class RLAgent:
    # ------------------------------------------------------------------------------------------------------------------
    # 全局
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # 内部变量+初始化
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,id):
        self.id = id
        #路口基本信息
        self.laneNum = 0 #车道数
        self.phaseNum = 0 #相位个数，或split个数
        self.phaseList = [] #有效的相位序号列表
        self.greenlimit = {'lower':3, 'upper':50}  #最小绿灯时长；最大绿灯时长
        #Q表
        initQT = {'keep':0.0, 'switch':0.0}
        self.QT = {}
        for num in range(0, 100):
            self.QT[num] = initQT

        #记录表: 记录step，state，action；每步仿真的状态和动作记录
        self.StepRecorder = {}
        # SSA = {}
        # SSA['state'] = 0
        # SSA['action'] = 'keep'
        # StepRecorder[0] = SSA

    # ------------------------------------------------------------------------------------------------------------------
    # 存储+读取
    # ------------------------------------------------------------------------------------------------------------------
    #添加有效的相位编号
    def addPhase(self,phaseID):
        self.phaseList.append(phaseID)
    #设置相位数
    def setPhaseNum(self,phaseNum):
        self.phaseNum = phaseNum
    #读取相位数
    def getPhaseNum(self):
        pass
    #读取相位编号列表
    def getPhaseList(self):
        pass


    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------
    #关于路口的状态
    def determineTrafficState(self,currentData):#评价交通状态
        print()

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------
    #关于路口Agent的动作

    # ------------------------------------------------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------------------------------------------------------
    #关于奖励