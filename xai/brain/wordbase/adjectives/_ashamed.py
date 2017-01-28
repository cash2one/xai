

#calss header
class _ASHAMED():
	def __init__(self,): 
		self.name = "ASHAMED"
		self.definitions = [u'feeling guilty or embarrassed about something you have done or about a quality in your character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
