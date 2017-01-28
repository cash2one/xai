

#calss header
class _FRANTICALLY():
	def __init__(self,): 
		self.name = "FRANTICALLY"
		self.definitions = [u'done in a hurried way and in a state of excitement or confusion: ', u'in a way that is almost out of control because of extreme emotion, such as worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
