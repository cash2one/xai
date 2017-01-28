

#calss header
class _EVENLY():
	def __init__(self,): 
		self.name = "EVENLY"
		self.definitions = [u'If you say something evenly, you speak without showing emotion in your voice although you are angry or not satisfied in some way: ', u'in or into equal amounts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
