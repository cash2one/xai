

#calss header
class _INSTANTANEOUS():
	def __init__(self,): 
		self.name = "INSTANTANEOUS"
		self.definitions = [u'happening immediately, without any delay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
