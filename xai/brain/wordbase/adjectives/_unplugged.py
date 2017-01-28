

#calss header
class _UNPLUGGED():
	def __init__(self,): 
		self.name = "UNPLUGGED"
		self.definitions = [u'used to refer to musicians performing without electric instruments and without amplification (= electronic equipment that makes sound louder)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
