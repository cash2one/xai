

#calss header
class _AUTOMATICALLY():
	def __init__(self,): 
		self.name = "AUTOMATICALLY"
		self.definitions = [u'If a machine or device does something automatically, it does it independently, without human control: ', u'If you do something automatically, you do it without thinking about it: ', u'If something happens automatically, it happens as part of the normal process or system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
