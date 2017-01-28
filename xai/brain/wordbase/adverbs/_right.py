

#calss header
class _RIGHT():
	def __init__(self,): 
		self.name = "RIGHT"
		self.definitions = [u'on or towards the side of your body that is to the east when you are facing north: ', u'exactly or all the way: ', u'used for emphasis: ', u'immediately: ', u'at the present time: ', u'used as part of the title of particular people, such as bishops and some members of Parliament: ', u'correctly: ', u'If something goes right, it is successful or happens in a way that you hoped it would: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
