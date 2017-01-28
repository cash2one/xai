

#calss header
class _STREAMING():
	def __init__(self,): 
		self.name = "STREAMING"
		self.definitions = [u'If you have a streaming cold, your nose and eyes are producing a lot of liquid because you have a common infection.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
