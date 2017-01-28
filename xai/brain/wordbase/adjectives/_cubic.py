

#calss header
class _CUBIC():
	def __init__(self,): 
		self.name = "CUBIC"
		self.definitions = [u'used in units of volume to show when the length of something has been multiplied by its width and height']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
