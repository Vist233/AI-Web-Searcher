整体的实现路径是：
用户输入query
LLM根据query选择合适的searchPara调用Search工具
Search MCP接收到searchPara开始处理
    searchPara分并行分发给3个小模型（3-7B，或者是flash），分别搜索到5个结果(orderNum, title, url, abstract),小模型根据内容返回选择合适的orderNum
    系统根据orderNum从五个结果中取得合适的结果(orderNum, title, url, abstract)，这3个模型的处理结果重新编排orderNum交给主模型（这是个大模型，至少70B）。
    主模型根据输入，返回合适的Number，将结果（只有前三个内容带上content）返回。