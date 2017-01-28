

#calss header
class _ROUTINE():
	def __init__(self,): 
		self.name = "ROUTINE"
		self.definitions = [u'done as part of what usually happens, and not for any special reason: ', u'ordinary and not special or unusual: ', u'ordinary and boring: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
