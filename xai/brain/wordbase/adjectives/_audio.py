

#calss header
class _AUDIO():
	def __init__(self,): 
		self.name = "AUDIO"
		self.definitions = [u'connected with sound and the recording and broadcasting of sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
