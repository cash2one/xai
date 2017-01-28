

#calss header
class _INSIPID():
	def __init__(self,): 
		self.name = "INSIPID"
		self.definitions = [u'not having a strong taste or character, or having no interest or energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
