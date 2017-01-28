

#calss header
class _INDISPENSABLE():
	def __init__(self,): 
		self.name = "INDISPENSABLE"
		self.definitions = [u'Something or someone that is indispensable is so good or important that you could not manage without it, him, or her: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
