

#calss header
class _PERT():
	def __init__(self,): 
		self.name = "PERT"
		self.definitions = [u'attractively small and firm, as a description of a part of the body: ', u'used to describe behaviour or qualities, especially in a young woman, that are humorous because they do not show much respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
