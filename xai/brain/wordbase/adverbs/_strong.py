

#calss header
class _STRONG():
	def __init__(self,): 
		self.name = "STRONG"
		self.definitions = [u'to behave towards another person in a way that is too severe, or that shows a strong sexual interest that the other person does not want: ', u'to make an extra effort in order to be successful or to have control in a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
