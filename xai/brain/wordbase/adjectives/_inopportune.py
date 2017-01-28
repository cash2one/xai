

#calss header
class _INOPPORTUNE():
	def __init__(self,): 
		self.name = "INOPPORTUNE"
		self.definitions = [u'happening or done at a time that is not suitable or convenient: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
