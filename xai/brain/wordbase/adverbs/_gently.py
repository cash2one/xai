

#calss header
class _GENTLY():
	def __init__(self,): 
		self.name = "GENTLY"
		self.definitions = [u'calmly, kindly, or softly: ', u'without force or strength: ', u'slightly or gradually: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
