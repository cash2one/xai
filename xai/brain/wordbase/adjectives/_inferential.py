

#calss header
class _INFERENTIAL():
	def __init__(self,): 
		self.name = "INFERENTIAL"
		self.definitions = [u'based on inference (= a guess or opinion that comes from the information that you have): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
