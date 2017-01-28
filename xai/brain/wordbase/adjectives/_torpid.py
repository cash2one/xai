

#calss header
class _TORPID():
	def __init__(self,): 
		self.name = "TORPID"
		self.definitions = [u'not active; moving or thinking slowly, especially as a result of being lazy or feeling that you want to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
