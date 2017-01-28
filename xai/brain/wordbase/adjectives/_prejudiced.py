

#calss header
class _PREJUDICED():
	def __init__(self,): 
		self.name = "PREJUDICED"
		self.definitions = [u'showing an unreasonable dislike for something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
