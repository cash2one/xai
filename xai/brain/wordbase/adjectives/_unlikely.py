

#calss header
class _UNLIKELY():
	def __init__(self,): 
		self.name = "UNLIKELY"
		self.definitions = [u'not probable or likely to happen: ', u'not the same as you would usually expect: ', u'probably not true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
