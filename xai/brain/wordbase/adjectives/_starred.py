

#calss header
class _STARRED():
	def __init__(self,): 
		self.name = "STARRED"
		self.definitions = [u'marked with an asterisk (= the symbol *): ', u'A starred hotel or restaurant is one that has been given one or more stars for quality.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
