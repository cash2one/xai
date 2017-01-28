

#calss header
class _DRUNK():
	def __init__(self,): 
		self.name = "DRUNK"
		self.definitions = [u'unable to speak or act in the usual way because of having had too much alcohol: ', u'the crime of behaving badly in public after drinking too much alcohol', u'having a strong and unreasonable feeling of being able to control other people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
