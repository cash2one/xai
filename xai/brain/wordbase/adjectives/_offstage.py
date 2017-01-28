

#calss header
class _OFFSTAGE():
	def __init__(self,): 
		self.name = "OFFSTAGE"
		self.definitions = [u'off the stage, or happening behind or at the side of the stage, so that people who are watching cannot see: ', u'used to describe a performer when they are not performing in a play or film, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
