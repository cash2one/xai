

#calss header
class _LIGHTLY():
	def __init__(self,): 
		self.name = "LIGHTLY"
		self.definitions = [u'gently: ', u'If food is lightly cooked, it is cooked for only a short time: ', u'If you say something lightly, you are not serious when you say it: ', u'If something is not said or treated lightly, it is said or treated in a serious way, after great thought: ', u'to be punished or to punish someone less severely than might have been expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
