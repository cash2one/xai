

#calss header
class _NAUSEATING():
	def __init__(self,): 
		self.name = "NAUSEATING"
		self.definitions = [u'making you feel as if you are going to vomit: ', u"If someone's opinions or actions are nauseating, you dislike and disapprove of them: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
