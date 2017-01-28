

#calss header
class _FULL():
	def __init__(self,): 
		self.name = "FULL"
		self.definitions = [u'(of a container or a space) holding or containing as much as possible or a lot: ', u'containing a lot of things or people or a lot of something: ', u'involving a lot of activities: ', u'to be talking or thinking a lot about something that you have enjoyed or found exciting: ', u'to think and act as if you are very important: ', u'to think that you are very important in a way that annoys other people: ', u'complete, whole, or containing a lot of detail: ', u'completely: ', u'If an activity is in full flow, it is happening fast and with energy: ', u'If an event is in full swing, it has already been happening for a period of time and there is a lot of activity: ', u'able to be seen by other people: ', u'the greatest possible: ', u'having eaten so much food that you cannot eat any more: ', u'having recently eaten: ', u'(of clothing) loose or containing a lot of material, or (of parts of the body) quite large and rounded: ', u'used to avoid saying "fat": ', u'(of a flavour, sound, smell, etc.) strong or deep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
