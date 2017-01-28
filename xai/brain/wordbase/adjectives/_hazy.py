

#calss header
class _HAZY():
	def __init__(self,): 
		self.name = "HAZY"
		self.definitions = [u'Hazy air or weather is not clear, especially because of heat: ', u'not remembering things clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
