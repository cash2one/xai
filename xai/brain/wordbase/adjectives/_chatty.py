

#calss header
class _CHATTY():
	def __init__(self,): 
		self.name = "CHATTY"
		self.definitions = [u'liking to talk a lot in a friendly, informal way', u'If a piece of writing is chatty, it is informal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
