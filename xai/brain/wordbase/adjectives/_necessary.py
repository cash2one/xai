

#calss header
class _NECESSARY():
	def __init__(self,): 
		self.name = "NECESSARY"
		self.definitions = [u'needed in order to achieve a particular result: ', u'used in negatives and questions to show that you disapprove of something and do not think it should be used or done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
