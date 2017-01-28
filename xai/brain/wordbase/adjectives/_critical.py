

#calss header
class _CRITICAL():
	def __init__(self,): 
		self.name = "CRITICAL"
		self.definitions = [u'saying that someone or something is bad or wrong: ', u'of the greatest importance to the way things might happen: ', u'giving opinions or judgments on books, plays, films, etc.: ', u'extremely serious or dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
